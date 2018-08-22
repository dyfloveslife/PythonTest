class Home:
    def __init__(self, new_area, new_style, new_addr):
        self.area = new_area
        self.style = new_style
        self.addr = new_addr
        self.left_area = new_area
        self.contain_items = []

    def __str__(self):
        message = '房子的面积是%d,可用面积是%d,户型是%s,地址是%s' % (self.area, self.left_area, self.style, self.addr)
        message += '房子里有%s' % str(self.contain_items)
        return message

    def add_item(self, item):
        """
        将床放到房子中。
        :param self: 房子
        :param item: 床
        :return:
        """
        # self.left_area -= item.area
        # self.contain_items.append(item.name)
        self.left_area -= item.get_area()  # 便于以后取值
        self.contain_items.append(item.get_name())


class Bed:
    def __init__(self, new_name, new_area):
        self.name = new_name
        self.area = new_area

    def __str__(self):
        return '%s占用面积是%d' % (self.name, self.area)

    def get_area(self):
        """
        :return: 床的面积
        """
        return self.area

    def get_name(self):
        """
        :return: 床的名字
        """
        return self.name


bad1 = Bed('席梦思', 3)
bad2 = Bed('小天鹅', 6)
print(bad1)
print(bad2)

house = Home(130, '三室一厅', '北京市朝阳区123号')
print(house)

house.add_item(bad1)
house.add_item(bad2)
print(house)
