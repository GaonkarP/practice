def count_sock_pair(my_li):
  my_se = set(my_li)
  num_pair = 0

  for itm in my_se:
      num_pair = num_pair + int(my_li.count(itm)/2)

  print(num_pair)
  
  
 def hill_or_valley(my_str):
  up_count = 0
  dw_count = 0
  ground_level = True
  val_count = 0
  mount_count = 0

  for char in my_str:
      if ground_level:
          if char =="U":
              mount_count +=1
          else:
              val_count +=1
      if char =="U":
          up_count += 1
          ground_level = False
      if char =="D":
          dw_count += 1
          ground_level = False
      if up_count == dw_count : 
          ground_level = True
          up_count = 0
          dw_count = 0

  print(mount_count)
  print(val_count)
