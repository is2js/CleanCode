class CompositeDict:
    def __init__(self, policy_data, **extra_data):
        # dict파라미터를 키워드파라미터와 합친 dict를 만드는 법
        self._data = {**policy_data, **extra_data}

    # 소유한 dict인 _data에 대한 setter
    def change_in_policy(self, customer_id, **new_policy_data):
        # update()는 keyword 파라미터로 기존 dict value를 덮어쓴다.
        self._data[customer_id].update(**new_policy_data)

    # dict일급컬렉션의 내부자료구조를 객체로 []인덱싱(첨자기능)하게 한다.
    # -> getitem + len
    def __getitem__(self, customer_id):
        return self._data[customer_id]

    def __len__(self):
        return len(self._data)
