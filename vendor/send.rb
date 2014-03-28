require "faker"
require "i18n"
require "net/http"

TARGET_URL = "http://localhost:5000/student-add"
TEST_URL   = "http://localhost:5000/classroom"

TESTS      = %w[jun nov center jan mar]

I18n.enforce_available_locales = false
I18n.locale = :ja

include Faker

def network_alive?
  res = Net::HTTP.get_response URI(TARGET_URL)
  res.class == Net::HTTPNotFound
end

def test_is test
	case test
	when "jun"	then Date.new(2013, 6, rand(10..12))
	when "nov"	then Date.new(2013, 9, rand(20..22))
	when "center"	then Date.new(2013, 11, rand(10..12))
	when "jan"	then Date.new(2014, 1, rand(20..22))
	when "mar"	then Date.new(2014, 3, rand(10..12))
	end
end

Net::HTTP.get(URI.parse('http://localhost:5000/deleteall'))

students = []
%w[A B C D].each do |klass|
  ary = []
  20.times do |num|
    h = {studentname: Name.name,
         studentnum:  num+1,
         classroom:   klass}

    ary << h
  end
  students += ary
end

success, failure = [], []
students.each_with_index do |student, i|
  response = Net::HTTP.post_form(URI.parse(TARGET_URL), student)

  TESTS.each do |test|
	h = {}
	h[:summary] = test
	%w[math english science social language].each do |s|
		h[(s + "datetime").to_sym]  = test_is(test).strftime('%F')
		score_h = 100 * rand(0.5..0.99)
		h[(s + "score").to_sym] = score_h.floor.to_s
	end
	url = "#{TEST_URL}/#{student[:classroom]}/#{student[:studentnum]}"
	resp = Net::HTTP.post_form(URI.parse(url), h)
	resp.code == "200" ? success.<<(true) : failure.<<(true)
  end

  response.code == "200" ? success.<<(true) : failure.<<(true)
  print "student #{i} was sent\r"
end

puts "done!                   "
puts "success: #{success.size}"
puts "failure: #{failure.size}"
