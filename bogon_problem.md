http://air20.com/archives/486.html
>> 如题，Mac 下的终端经常有时候前面的计算机名会错误的显示成 bogon.
>> 是因为终端会先向 DNS 请求查询当前 IP 的反向域名解析的结果，
>> 如果查询不到再显示我们设置的计算机名。
>> 而由于我们的 DNS 错误地将保留地址反向的 NS 查询结果返回了 bogon. 
>> 其中 bogon 本应该用来指虚假的 IP 地址，
>> 而非保留 IP 地址。因此就出现了会时不时地打印 bogon
>> 这种奇怪名字作为计算机名的现象了。
>> 那么如何让终端只显示我们想要的计算机名而不总是从 DNS 返回结果呢？
>> 
>> 解决方案：
>> 在终端中执行以下命令即可（需要输入一次管理员密码）
>> 
>> ```
>> sudo hostname your-desired-host-name
>> sudo scutil --set LocalHostName $(hostname)
>> sudo scutil --set HostName $(hostname)
>> ```
