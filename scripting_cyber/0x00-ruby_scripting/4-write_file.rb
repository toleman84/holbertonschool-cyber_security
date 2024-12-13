#!/usr/bin/env ruby
require 'json'

def merge_json_files(file1_path, file2_path)
    file_content_1 = File.read(file1_path)
    file_content_2 = File.read(file2_path)
    data1 = JSON.parse(file_content_1)
    data2 = JSON.parse(file_content_2)

    merge_data = data1.merge(data2)

    user_id_count = Hash.new(0)

    merge_data.each do |item|
        user_id_count[item["userId"]] += 1
    end

    user_id_count.each do |user_id, count|
        puts "#{user_id}: #{count}"
    end
end
