element = ('q', 'w', 'e')
spell = [[fir, sec, thi]for fir in element for sec in element
         for thi in element]
skill_list = []
for skill in spell:
    skill.sort()
    if skill not in skill_list:
        skill_list.append(skill)
print(f'卡尔技能数量为：{len(skill_list)}')
for i in skill_list:
    print(i)
