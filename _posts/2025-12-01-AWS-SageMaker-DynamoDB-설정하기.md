---
title: AWS SageMaker 및 DynamoDB 설정하기
date: 2025-12-01 09:15:00 +0900
categories: ['정리']
tags: ['aws', 'sagemaker', 'dynamodb', 'deployment']
author: lim4349
---

# AWS SageMaker 및 DynamoDB 설정하기

회사에서 챗봇을 AWS에 배포하기 위해 SageMaker와 DynamoDB를 설정한 과정을 정리합니다.

> **참고**: 본 문서의 모든 설정은 **버지니아 리전(us-east-1)**에서 진행되었습니다. 따라서 문서 내의 모든 AWS 콘솔 링크는 `us-east-1` 리전으로 설정되어 있습니다. 다른 리전을 사용하는 경우 링크의 리전 부분을 해당 리전으로 변경하시기 바랍니다.

## 요구사항

- 업로드 문서가 도메인이 고정되어 있지 않음
- 각 유저가 히스토리를 가져야 함
- 원래는 길면 LLM으로 요약하려 했으나, 최근 3개만 사용하기로 결정
- 저장을 위해 **DynamoDB** 사용
- LLM모델은 AWS에 올리는 겸 **SageMaker** 사용해보기로 함

## 사전 준비

인터넷에 수많은 자료가 있으나 초심자에게는 외계어와 같았습니다. 사용하라는 명령어는 SageMaker Studio 노트북에서 치라는 건지, 로컬에서 치라는 건지, SageMaker AI는 왜 또 분리되어 있는 건지, IAM, ARN, Role, Policy 등 알아야 할 사전지식이 너무 많았습니다.

대충 기억나는 순서대로 정리해봅니다.

### 작업 순서

1. 로컬에 RAG 서버는 FastAPI로 구축하고 pytest로 테스트 완료
2. DynamoDB 세팅하고 AWS에 RAG 서버 올려놓고 DB 연결 확인
3. SageMaker 연결하고 최종 확인

## 1. DynamoDB 만들기

DynamoDB는 AWS 콘솔에서 간단하게 생성할 수 있습니다.

1. [DynamoDB 콘솔](https://us-east-1.console.aws.amazon.com/dynamodbv2/home?region=us-east-1#dashboard)에 접속
2. 테이블 이름을 지정하고 생성

## 2. EC2에 Role 부여하기

EC2에 서버가 있고 거기서 접근해야 하므로 EC2에 Role을 부여해야 합니다.

### IAM Role 생성

1. [IAM 콘솔 - 역할](https://us-east-1.console.aws.amazon.com/iam/home?region=us-east-1#/roles)에 접속
2. **역할 생성** → **AWS 서비스** → **사용 사례: EC2** 선택
3. 권한 정책 추가:
   - `AmazonDynamoDBFullAccess`: DynamoDB 접근 권한
   - `AmazonSageMakerFullAccess`: SageMaker 접근 권한 (EC2가 SageMaker를 사용해야 하므로)

### 신뢰 관계 설정

IAM → 역할 → **신뢰 관계** → **신뢰할 수 있는 엔티티**에서 JSON으로 편집:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "sagemaker.amazonaws.com",
                    "ec2.amazonaws.com"
                ]
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

**중요**: `"sagemaker.amazonaws.com"` 한 줄을 추가해야 합니다.

### ARN 확인 및 EC2에 적용

생성된 Role의 ARN 형식:

```
arn:aws:iam::(계정 아이디):role/(지정한 IAM 이름)
```

EC2 대시보드에서:
1. 원하는 인스턴스 선택
2. **작업** → **보안** → **IAM 역할 수정**
3. 생성한 Role 지정

## 3. SageMaker 올리기

이 부분이 가장 문제였습니다. 사수분의 개인 GitHub에 Docker로 한번에 묶어서 모든 걸 해주는 모범 답안이 있었지만, 그럼 재미없으니까 직접 헤딩해보기로 했습니다.

### SageMaker 실행 환경의 차이

웹페이지에서 제공하는 Studio에서 사용했었는데, endpoint를 만들려면 모델 등록부터 해야 하고, 모델 올리는 스크립트는 어디서 실행해야 하는지 한참 헤맸습니다.

**핵심 차이점**:

1. **AWS SageMaker Studio에서 실행**: Role 같은 것을 Studio에서 하면 알아서 연동되어 있는 것을 가져옵니다.
2. **로컬이나 다른 곳에서 실행**: 스크립트를 짜려면 귀찮은 설정을 직접 가져와서 `.env`든 `properties`든에 만들어서 직접 넣어줘야 합니다.

**어디서 돌리냐에 따라 준비가 약간 달라집니다.**

개인적으로는 그냥 사이트 말고 CLI로 올리는 게 편합니다. SageMaker 웹에서 노트북 실행하는 것만 한 3군데 있었는데, 이게 왜 굳이 나눠져 있고 여러 개 있는지 이해를 못해버렸습니다.

### 용어 정리

- **LMI (Large Model Inference)**: 대규모 모델 추론을 위한 AWS의 컨테이너 시스템입니다. vLLM, TensorRT-LLM 등을 지원합니다.
  - 참고: [AWS 공식 문서 - Large Model Inference Container](https://docs.aws.amazon.com/ko_kr/sagemaker/latest/dg/large-model-inference-container-docs.html)

- **DJL (Deep Java Library)**: Java 개발자를 위한 오픈 소스 딥러닝 라이브러리로, SageMaker에서 모델 배포를 간소화합니다.
  - 참고: [AWS 공식 문서 - DJL Serving으로 모델 배포하기](https://docs.aws.amazon.com/ko_kr/sagemaker/latest/dg/deploy-models-frameworks-djl-serving.html)


### 모델 배포 코드

우리는 vLLM으로 서빙된 것을 쓸 거니까 그걸 지원하는 버전도 찾아야 하고, Qwen3 4B Instruct 2507 버전이 또 안 되어서 직접 모델을 올려줘야 했습니다.

```python
from sagemaker import image_uris, Model
import sagemaker

# 컨테이너 URI 가져오기
container_uri = image_uris.retrieve(
    framework="djl-lmi",
    region=AWS_REGION,
    version=lmi_version,
)

# 모델 생성
model = Model(
    image_uri=container_uri,
    role=ROLE_ARN,
    env=MODEL_ENV,
    sagemaker_session=sm_session,
    name=MODEL_ID.replace("/", "-"),
)

# =========================
# 엔드포인트 배포
# =========================
predictor = model.deploy(
    initial_instance_count=1,
    instance_type=INSTANCE_TYPE,
    endpoint_name=ENDPOINT_NAME,
    wait=True,
    container_startup_health_check_timeout=600,  # 헬스체크 타임아웃: 600초 (10분)
)
```

### 환경 변수 설정

```bash
export AWS_REGION=us-east-1
export SAGEMAKER_EXECUTION_ROLE_ARN=(아까 위에서 만든 ARN)
export HF_MODEL_ID=Qwen/Qwen3-4B-Instruct-2507
export SAGEMAKER_INSTANCE_TYPE=ml.g5.xlarge
export SAGEMAKER_ENDPOINT_NAME=(지정할 엔드포인트 이름)
export OPTION_MAX_ROLLING_BATCH_SIZE=1
export TENSOR_PARALLEL_DEGREE=1
export OPTION_TRUST_REMOTE_CODE=true
export OPTION_MAX_MODEL_LEN=4096
export LMI_VERSION=0.35.0
export CONTAINER_STARTUP_TIMEOUT=600
```

### 배포 시 주의사항

몇 번씩 에러가 발생했는데, 알고 보니 인자 이름이 달라서 `max_len`이 설정해도 계속 터지고 있던 것입니다.

로그를 보면:

```
[INFO] 수동 구성 완료: 763104351884.dkr.ecr.us-east-1.amazonaws.com/djl-inference:0.35.0-lmi17.0.0-cu128
[INFO] Using container_uri: 763104351884.dkr.ecr.us-east-1.amazonaws.com/djl-inference:0.35.0-lmi17.0.0-cu128
```

이걸로 수동 구성했다고 나옵니다. 해당 버전을 미리 찾아서 원하는 버전을 명시하는게 중요해 보입니다.

**인스턴스 타입**: `ml.g5.xlarge`는 VRAM 24GiB짜리라 많은 처리는 안 되는데, 일단 올려보는 게 목적이라 테스트하고 있습니다.

이렇게 올리는 것과 Docker로 올리는 것의 장/단점, 차이점, 특징은 추후에 확인해봐야겠습니다.

## 4. 배포 확인

Deploy되고 pytest하니 잘 통과합니다.

### CloudWatch 로그 확인

[AWS CloudWatch 콘솔](https://us-east-1.console.aws.amazon.com/cloudwatch/)에서 SageMaker를 찾아서 **로그 스트림**을 누르면 로그 이벤트가 줄줄이 표시됩니다.

SageMaker가 비싼 대신 다 관리해준다고 하니 좋긴 합니다. 필터링도 되고 다 좋은데, 입/출력 같은 건 안 뜨나 봅니다. 이건 EC2 서버에서 보이게 해야겠습니다.

## 참고 자료

- [AWS SageMaker 공식 문서 - Large Model Inference Container](https://docs.aws.amazon.com/ko_kr/sagemaker/latest/dg/large-model-inference-container-docs.html)
- [AWS DynamoDB 콘솔](https://us-east-1.console.aws.amazon.com/dynamodbv2/home?region=us-east-1#dashboard)
- [AWS IAM 콘솔 - 역할](https://us-east-1.console.aws.amazon.com/iam/home?region=us-east-1#/roles)
- [AWS CloudWatch 콘솔](https://us-east-1.console.aws.amazon.com/cloudwatch/)

## FAQ

- **ARN이 뭔가요?**
  - **ARN (Amazon Resource Name)**: AWS 리소스를 특정하기 위한 주소입니다. 형식은 `arn:aws:서비스:리전:계정ID:리소스타입/리소스이름`입니다.

- **IAM이 뭔가요?**
  - **IAM (Identity and Access Management)**: AWS에서 접근 권한을 관리하는 서비스입니다. 사용자, 그룹, 역할, 정책을 통해 AWS 리소스에 대한 접근을 제어합니다.

- **Role이 뭔가요?**
  - **Role**: 임시 권한을 제공하는 역할입니다. 사람이나 서비스(EC2, SageMaker 등) 모두 사용할 수 있습니다. Role을 부여받으면 해당 권한을 사용할 수 있습니다.

- **Policy가 뭔가요?**
  - **Policy**: 실제 권한을 적은 JSON 문서입니다. 어떤 리소스에 어떤 작업을 허용할지 명시합니다.

- **LMI와 DJL이 뭔가요?**
  - **LMI (Large Model Inference)**: 대규모 모델 추론을 위한 AWS의 컨테이너 시스템입니다.
  - **DJL (Deep Java Library)**: AWS에서 제공하는 딥러닝 프레임워크로, LMI 컨테이너에서 사용됩니다.

- **EC2에 Role을 부여하는 이유는?**
  - EC2 인스턴스에서 DynamoDB나 SageMaker 같은 AWS 서비스에 접근하려면 권한이 필요합니다. Role을 부여하면 EC2 인스턴스가 해당 권한을 사용할 수 있습니다.

- **신뢰 관계(Trust Relationship)에서 `sagemaker.amazonaws.com`을 추가하는 이유는?**
  - SageMaker 서비스가 이 Role을 사용할 수 있도록 허용하기 위함입니다. EC2만 추가하면 EC2에서만 사용 가능하고, SageMaker에서 사용하려면 SageMaker 서비스도 신뢰할 수 있는 엔티티에 추가해야 합니다.

## 총평

알아야 할 게 너무 많습니다. 그래도 하나씩 알아가니까 재밌습니다.

