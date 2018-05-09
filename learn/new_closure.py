def test(num):
    print("----1----")

    def test_in():
        print("----2----")
        print(num + 100)

    print("----3----")
    return test_in


if __name__ == '__main__':
    # 把函数引用赋值给ret
    ret = test(100)
    ret_2 = test(10)
    ret()
