#!/usr/bin/env ruby
#
# Give generated papers posts stable, date-based URLs.

Jekyll::Hooks.register :posts, :post_init do |post|
  basename = File.basename(post.path)

  case basename
  when /\A(\d{4}-\d{2}-\d{2})-daily-papers(?:-\d+)?\.md\z/
    post.data['permalink'] ||= "/posts/daily-papers-#{Regexp.last_match(1)}/"
  when /\A(\d{4})-(\d{2})-01-monthly-papers-summary\.md\z/
    post.data['permalink'] ||= "/posts/monthly-papers-summary-#{Regexp.last_match(1)}-#{Regexp.last_match(2)}/"
  end
end
