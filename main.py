from Bkgnd import Bkgnd
from TaskList import list



if __name__ == "__main__":
  # while (any(not obj.is_over for obj in list)):
    # 调用对象的属性和方法
    for obj in list:
      if (obj.is_over): continue
      
      print(f"任务名: {obj.name}, {'已完成' if obj.is_over else '剩余'+str(obj.num-obj.Done_unm)}")
      obj.fn()
    print('所有任务已完成')      