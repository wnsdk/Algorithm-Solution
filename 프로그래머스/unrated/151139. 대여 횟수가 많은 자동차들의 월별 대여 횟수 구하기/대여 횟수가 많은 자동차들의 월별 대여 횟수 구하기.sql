SELECT
    TO_NUMBER(TO_CHAR(start_date, 'MM')) AS MONTH
    , CAR_ID
    , COUNT(*) AS RECORDS
FROM
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE
    TO_CHAR(start_date, 'YYYY-MM') BETWEEN '2022-08' AND '2022-10'
    AND CAR_ID IN (
        SELECT
            CAR_ID
        FROM
            CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE
            TO_CHAR(start_date, 'YYYY-MM') BETWEEN '2022-08' AND '2022-10'
        GROUP BY
            CAR_ID
        HAVING
            COUNT(*) >= 5
    )
GROUP BY
    TO_CHAR(start_date, 'MM')
    , CAR_ID
HAVING
    COUNT(*) > 0
ORDER BY
    MONTH
    , CAR_ID DESC