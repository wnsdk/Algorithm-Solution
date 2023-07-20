SELECT YEAR(O.SALES_DATE) AS YEAR, MONTH(O.SALES_DATE) AS MONTH, U.GENDER AS GENDER, 
    COUNT(DISTINCT U.USER_ID) AS USERS
FROM USER_INFO U JOIN ONLINE_SALE O ON U.USER_ID = O.USER_ID
GROUP BY YEAR(O.SALES_DATE), MONTH(O.SALES_DATE), U.GENDER
HAVING U.GENDER IS NOT NULL
ORDER BY YEAR(O.SALES_DATE), MONTH(O.SALES_DATE), U.GENDER
