# coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
���ڣ�2020/11/21
"""

import random
comp_number = random.randrange(0, 4)
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name = input()



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��


def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if choice_name=="ʯͷ":
        return 0
    elif choice_name=="ʷ����":
        return 1
    elif choice_name=="ֽ":
        return 2
    elif choice_name=="����":
        return 3
    elif choice_name=="����":
        return 4
    else:
        return None


# ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
# ��Ҫ���Ƿ��ؽ��


player_choice_number=name_to_number



# ��дִ�д���,������ɺ�passɾ��


def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    comp_number = random.randrange(0, 4)
    if number == 0:
        return 'ʯͷ'
    elif number == 1:
        return 'ʷ����'
    elif number == 2:
        return '��'
    elif number == 3:
        return '����'
    elif number == 4:
        return '����'

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��
    # ��дִ�д���,������ɺ�passɾ��


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """



print("����ѡ��Ϊ��",choice_name)
comp_choice = number_to_name(comp_number)
choice_name=name_to_number(choice_name)
print('�������ѡ��Ϊ', comp_choice)
if choice_name ==comp_number:
    print("���ͼ��������һ����")
if choice_name == 0 and comp_number == 4:
    print("��Ӯ��")
if choice_name == 0 and comp_number == 3:
    print("��Ӯ��")
if choice_name == 0 and comp_number == 1:
    print("����Ӯ��")
if choice_name == 0 and comp_number == 2:
    print("����Ӯ��")
if choice_name == 1 and comp_number == 4:
    print("��Ӯ��")
if choice_name == 1 and comp_number == 0:
    print("��Ӯ��")
if choice_name == 1 and comp_number ==3:
    print("����Ӯ��")
if choice_name == 1 and comp_number == 2:
    print("����Ӯ��")
if choice_name == 2 and comp_number ==1:
    print("��Ӯ��")
if choice_name == 2 and comp_number == 0:
    print("��Ӯ��")
if choice_name == 2 and comp_number == 4:
    print("����Ӯ��")
if choice_name == 2 and comp_number == 3:
    print("����Ӯ��")
if choice_name == 3 and comp_number ==1:
    print("��Ӯ��")
if choice_name == 3 and comp_number == 2:
    print("��Ӯ��")
if choice_name == 3 and comp_number == 0:
    print("����Ӯ��")
if choice_name == 3 and comp_number ==4:
    print("����Ӯ��")
if choice_name == 4 and comp_number == 2:
    print("��Ӯ��")
if choice_name == 4 and comp_number == 3:
    print("��Ӯ��")
if choice_name == 4 and comp_number == 1:
    print("����Ӯ��")
if choice_name == 4 and comp_number == 0:
    print("����Ӯ��")




# ���"-------- "���зָ�
# ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

# ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

# ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

# ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

# ����Ļ����ʾ�����ѡ����������

# ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

# ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

# ����������ʾ��дִ�д��룬������ɺ�ɾ����pass


# �Գ�����в���
