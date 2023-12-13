with open('12.txt') as f:
    data = f.read().splitlines()

def count(row, nums):
    if (row, *nums) in seen:
        return seen[(row, *nums)]
    
    if nums == []:
        return 0 if '#' in row else 1
    
    if len(row) == 0:
        return 0 if nums != [] else 1

    counter = 0
    if row[0] in '#?' and len(row) >= nums[0] and '.' not in row[:nums[0]] and (len(row) == nums[0] or row[nums[0]] in '.?'):
        counter += count(row[nums[0]+1:], nums[1:])
    
    if row[0] in '.?':
        counter += count(row[1:], nums)

    seen[(row, *nums)] = counter
    return counter

seen = {}
total = 0
for line in data:
    row, nums = line.split()
    nums = [int(x) for x in nums.split(',')]

    total += count(row, nums)
print('Part 1:', total)

seen = {}
total = 0
for line in data:
    row, nums = line.split()
    nums = [int(x) for x in nums.split(',')]
    row = '?'.join([row] * 5)
    nums = [x for _ in range(5) for x in nums]

    total += count(row, nums)
print('Part 2:', total)