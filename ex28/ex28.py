print(" 1. True and True = %s" % str(True and True))
# true 'and' true is true
print(" 2. False and True = %s" % str(False and True))
# false 'and' true is false. false have importance with 'and'
print(" 3. 1==1 and 2==1 = %s" % ((1==1) and (2==1)))
# 1==1 is true, 2==1 is false, so answer is false. == means same
print(" 4. 'test' == 'test'= %s" % str('test' == 'test'))
# 'test' and 'test' are same. == can use with strings, not just number
print(" 5. 1==1 or 2!=1 = %s" % ((1==1) or (2 != 1)))
# 1==1 is true, 2!=1 is true. so answer is true. != means not same
print(" 6. True and 1==1 = %s" % str(True and (1==1)))
print(" 7. False and 0!=0 = %s" % str(False and (0 != 0)))
print(" 8. True or 1==1 = %s" % True or (1==1))
print(" 9. 'test' == 'testing' = %s" % str('test' == 'testing'))
print(" 10. 1!=0 and 2==1 = %s" % str((1 != 0)and (2 == 1)))
print(" 11. 'test'!='testing' = %s" % str('test' != 'testing'))
print(" 12. 'test'==1 = %s" % str('test'== 1))
print(" 13. not(True and False) = %s" % (not (True and False)))
# 'not' means opposite side. true and false is false, but not false is true
print(" 14. not(1==1 and 0!=1) = %s" % (not ((1 ==1) and (0 != 1))))
print(" 15. not(10==1 or 1000==1000) = %s" % (not ((10 == 1) or (1000 == 1000))))
print(" 16. not(1!=10 or 3==4) = %s" % (not ((1 != 10) or (3 == 4))))
print(" 17. not('testing'=='testing' and 'Zed'=='Cool Guy'= %s" % (
    not (('testing' == 'testing') and ('Zed' == 'Cool Guy'))))
print(" 18. 1==1 and not('testing'==1 or 1==0) = %s" % (
    (1 == 1) and not (('testing' == 1) or (1 == 0))))
print(" 19. 'chunky' == 'bacon' and not (3==4 or 3==3) = %s" % (
    ('chunky' == 'bacon' and not ((3 == 4) or (3 == 3)))))
print(" 20. 3==  and not('testing'=='testing' or 'Python'=='Fun') = %s" % (
    (3 == 3) and not (('testing' == 'testing') or ('Python' == 'Fun'))))

print("extra 1. 'test' and 'test' = = %s" % str('test' and 'test'))
# 'test' and 'test' are same. same words with 'and', print word.
print("extra 2. 1 and 1 = = %s" % str(1 and 1))
# like strings, numbers are same. same numbers print number.
print("extra 3. False and 1 = = %s" % str(False and 1))
# false and 1 are not same. not same is false so print false
print("extra 4. True and 1 = = %s" % str(True and 1))
# true and 1 are not same. so it is false but there is no false. this situation, it's printing 1