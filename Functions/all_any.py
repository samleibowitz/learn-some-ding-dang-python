people=['charlie','casey','cody','clare','christian']

all([names[0]=='c' for names in people]) ##true


nums = [2,60,26,18,21]

any([num%2==1  for num in nums]) ##true at least 1 is divisible by 2

type('d')