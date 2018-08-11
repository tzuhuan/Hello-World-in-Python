import multiprocessing as mp
import threading as td
import time

def job(q):
    print('job')
    res = 0
    for i in range(100000):
        res += i + i**2 + i**3
    # queue
    q.put(res)
    
def multicore():
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print('core: ', res1 + res2)

def normal():
    res = 0
    for _ in range(2):
        for i in range(100):
            res += i + i**2 + i**3
    print ('normal: ', res)

def multithread():
    q = mp.Queue()
    p1 = td.Thread(target=job, args=(q,))
    p2 = td.Thread(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print('thread: ', res1 + res2)

def job2(x):
    return x*x
    
def multicore_pool():
    pool = mp.Pool()
    res = pool.map(job2, range(100))
    print(res)
    res = pool.apply_async(job2, (2,))
    print(res.get())
    multi_res = [pool.apply_async(job2, (i,)) for i in range(100)]
    print([res.get() for res in multi_res])
    
def profile():
    st = time.time()
    normal()
    st1 = time.time()
    print('normal time: ', st1 - st)
    multithread()
    st2 = time.time()
    print('normal time: ', st2 - st1)
    multicore()
    print('normal time: ', time.time() - st2)
   
def job3(v, num, l):
    l.acquire()
    for _ in range(10):
        time.sleep(0.1)
        v.value += num
        print(v.value)
    l.release()
    
def multicore_lock():
    l = mp.Lock()
    v = mp.Value('i',0)
    p1 = mp.Process(target=job3, args=(v,1, l))
    p2 = mp.Process(target=job3, args=(v,3, l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
if __name__ == '__main__':
    #profile()
    #multicore_pool()
    multicore_lock()


