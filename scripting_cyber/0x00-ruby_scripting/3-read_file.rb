#!/usr/bin/env ruby
require 'json'

def count_user_ids(path)
    file_content = File.read(path)
    data = JSON.parse(file_content)
    user_id_count = Hash.new(0)

    data.each do |item|
        user_id_count[item["userId"]] += 1
    end

    user_id_count.each do |user_id, count|
        puts "#{user_id}: #{count}"
    end
end
