SELECT pro_name, pro_price
   FROM PRODUCT
   WHERE pro_price = 
    (SELECT MIN(pro_price) FROM PRODUCT);
SELECT pro_name, pro_price
   FROM PRODUCT
   WHERE pro_price = 
    (SELECT MAX(pro_price) FROM PRODUCT);    