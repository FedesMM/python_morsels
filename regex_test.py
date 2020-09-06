import re
m = re.findall('#\w+', 'balh balha hañsdhflkajsdñ 5466asdf  #hasdfa_asdfasf  asdfashdflkjh asdfasd asdfkjhalksdd halkjsh #asdjfhlaksd  asdfasd f')
print(m)


m = re.sub('#\w+', 'HASHTAG', 'balh balha hañsdhflkajsdñ 5466asdf  #hasdfa_asdfasf  asdfashdflkjh asdfasd asdfkjhalksdd halkjsh #asdjfhlaksd  asdfasd f')
print(m)

pattern = re.compile(r'(.*)#\w+')
m = pattern.sub(r"HASHTAG", 'balh balha hañsdhflkajsdñ 5466asdf  #hasdfa_asdfasf  asdfashdflkjh asdfasd asdfkjhalksdd halkjsh #asdjfhlaksd  asdfasd f', count=10)
print(m)