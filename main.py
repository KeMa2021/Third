import os
from multiprocessing import Pool

def callshell(name):
    print("call "+name)
    
    
class Func(object):
    def __init__(self):
        # 利用匿名函数模拟一个不可序列化象
        # 更常见的错误写法是，在这里初始化一个数据库的长链接
        self.num = lambda: None

    def work(self, num=None):
        self.num = num
        return self.num

    @staticmethod
    def call_back(res):
        print(f'Hello,World! {res}')

    @staticmethod
    def err_call_back(err):
        print(f'出错啦~ error：{str(err)}')
    

if __name__ == '__main__':
    programs=["a","b","c","d","e","f","g","h"]
    cmd = "touch result/{}.txt&& chmod 777 result/{}.txt&&./print.sh {} {} 2>&1 > result/{}.txt"
    
    for i in range(3):
        pool=Pool(processes =5)
        for program in programs:
            print("touch result/%s.txt&& chmod 777 result/%s.txt&&./print.sh %s %s 2>&1 > result/%s.txt"%(program,program,program,str(i),program))
            pool.apply_async(os.system,args=(cmd.format(program,program,program,str(i),program),),callback=Func.call_back,error_callback=Func.err_call_back)
            #pool.apply_async(os.system(cmd.format(program,program,program,str(i),program)))
        pool.close()
        pool.join()
        os.system("mkdir "+str(i)+"&& cp -r ./result/ ./"+str(i)+ " &&rm -r ./result && mkdir result")
