# frozen_string_literal: true

source "https://rubygems.org"

# Jekyll 4.x 사용 (GitHub Actions에서 빌드)
gem "jekyll", "~> 4.3"

# Jekyll Chirpy 테마 의존성
gem "jekyll-theme-chirpy", "~> 7.3"

# 추가 플러그인들
gem "jekyll-paginate", "~> 1.1"
gem "jekyll-seo-tag", "~> 2.8"
gem "jekyll-archives", "~> 2.2"
gem "jekyll-sitemap", "~> 1.4"
gem "jekyll-include-cache", "~> 0.2"

# 테스트용
gem "html-proofer", "~> 5.0", group: :test

# 플랫폼별 의존성
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

gem "wdm", "~> 0.2.0", :platforms => [:mingw, :x64_mingw, :mswin]
