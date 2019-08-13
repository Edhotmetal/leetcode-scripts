# Given n non-negative integers a1, a2, ..., an , where each represents a point at a coordinate (i, ai)
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with the x-axis forms a container, such that the container contains the most water.

class WaterContainer
	attr_accessor :heights # The list of integers that represent the heights of the walls of the container
	attr_accessor :max # Stores the indexes of the largest container and its area

	def initialize(heights)
		@heights = heights
		@length = heights.length
		@max = {indexes: [0,0], area: 0}
		find_max_area
	end

	def find_max_area()
		# This loop iterates through the list finding the largest area between two vertical lines
		# Starts at either end and works towards the middle for more efficiency

		area = 0 # Current area being compared

		i = 0
		j = @heights.length - 1

		while(i < j) do
			puts("i: #{i}\nj: #{j}")
			if(@heights[i] < @heights[j]) then
				area = @heights[i] * (j - i)
			else
				area = @heights[j] * (j - i)
			end
			if(@max[:area] < area) then
				puts("#{area} is greater than #{@max[:area]}!!")
				@max[:area] = area
				@max[:indexes] = [i,j]
			else
				puts("#{area} is not greater than #{@max[:area]}!!")
			end
			if(@heights[i] < @heights[j]) then
				i += 1
			else
				j -= 1
			end
		end
		puts("Max area is between (#{@max[:indexes][0]}, #{@heights[@max[:indexes][0]]}) and (#{@max[:indexes][1]}, #{@heights[@max[:indexes][1]]}) with an area of #{@max[:area]}")
	end
end

if(ARGV.length == 0) then
	puts("                 ~~~~~~~~~~water_container.rb~~~~~~~~~~")
	puts("This script receives a list of integers representing the potential walls of a container of water")
	puts("The script then returns the area of the largets container that can be made from the data")
	puts("Usage: ruby water_container.rb <int1> <int2> ... <intn>")
else
	args = Array.new # Place integer arguments into list and pass into find_max_area
	for arg in ARGV do
		begin
			args.push(arg.to_i)
		rescue ValueError
			puts("#{arg} is not an integer")
		end
	end

	if(args.length == 0) then
		puts("Please input a list of integers. Execute the script without arguments for help.")
	else
		container = WaterContainer.new(args)
		puts(container.max)
	end
end
