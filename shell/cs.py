import mysql.connector
def mysqlcon(sql,flag,base):
    if base == "sspanel":
        user = "sspanel"
        passwd = "iN3K8YjszyKX48HT"
    else:
        user = "pmxu_xyz"
        passwd = "Fwi5D2iYzXkw3kYN"
    mydb = mysql.connector.connect(
      
      host="localhost",       # 数据库主机地址
      user=user,    # 数据库用户名
      passwd=passwd,   # 数据库密码
      database=base
    )
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    if(flag):
        mydb.commit()
    else:
        res = mycursor.fetchall()
        return res

def cs():
    sql1 = "select `user_name`, `email`, `pass`, `passwd`, `uuid`, `u`, `d`, `transfer_enable`, `port`, `last_detect_ban_time`, `all_detect_number`, `last_check_in_time`, `reg_date`, `invite_num`, `money`, `ref_by`, `method`, `reg_ip`, `node_speedlimit`, `is_admin`, `im_type`, `im_value`, `class`, `class_expire`, `expire_in`, `theme`, `ga_token`, `ga_enable`, `remark`, `node_group`, `telegram_id`, `expire_notified`, `traffic_notified`, `forbidden_ip`, `forbidden_port`, `auto_reset_day`, `auto_reset_bandwidth` from user;"
    res = mysqlcon(sql1,False,'pmxu_xyz')
    for data in res:
        sql2 = "INSERT INTO `user` (`user_name`, `email`, `pass`, `passwd`, `uuid`, `u`, `d`, `transfer_enable`, `port`, `last_detect_ban_time`, `all_detect_number`, `last_check_in_time`, `reg_date`, `invite_num`, `money`, `ref_by`, `method`, `reg_ip`, `node_speedlimit`, `is_admin`, `im_type`, `im_value`, `class`, `class_expire`, `expire_in`, `theme`, `ga_token`, `ga_enable`, `remark`, `node_group`, `telegram_id`, `expire_notified`, `traffic_notified`, `forbidden_ip`, `forbidden_port`, `auto_reset_day`, `auto_reset_bandwidth`) VALUES ("
        sql2_tmp1 = ""
        for one in data:
            sql2_tmp1 = sql2_tmp1 + '"' + str(one) + '",'
        sql2 = sql2 + sql2_tmp1[0:-1] + ");"
        print(sql2)
        mysqlcon(sql2,True,'sspanel')
    

cs()