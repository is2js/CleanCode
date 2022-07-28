from CompositeDict import CompositeDict

if __name__ == '__main__':
    composite_dict = CompositeDict({1:{}, 2:{}}, 여분="더미", 여분2="더미2")
    print(composite_dict[1])
    composite_dict.change_in_policy(1, 이름="조재성", 나이=36)
    print(composite_dict[1])
    composite_dict.change_in_policy(1, 이름="김석영", 나이=35)
    print(composite_dict[1])