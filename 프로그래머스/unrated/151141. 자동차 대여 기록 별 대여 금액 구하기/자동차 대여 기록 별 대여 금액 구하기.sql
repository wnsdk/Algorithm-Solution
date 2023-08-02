SELECT
    H.HISTORY_ID AS HISTORY_ID,
    TRUNC(C.DAILY_FEE * H.DIFF * (100 - H.DISCOUNT_RATE) / 100) AS FEE
FROM 
    CAR_RENTAL_COMPANY_CAR C,
    (
        SELECT
            HISTORY_ID,
            CAR_ID,
            END_DATE - START_DATE + 1 AS DIFF,
            END_DATE,START_DATE,
            CASE 
                WHEN END_DATE - START_DATE + 1 >= 90
                THEN (
                    SELECT DISCOUNT_RATE
                    FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                    WHERE 
                        TO_NUMBER(REPLACE(DURATION_TYPE, '일 이상')) = 90
                        AND CAR_TYPE = '트럭'
                )
                WHEN END_DATE - START_DATE + 1 >= 30
                THEN (
                    SELECT DISCOUNT_RATE
                    FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                    WHERE 
                        TO_NUMBER(REPLACE(DURATION_TYPE, '일 이상')) = 30
                        AND CAR_TYPE = '트럭'
                )
                WHEN END_DATE - START_DATE + 1 >= 7
                THEN (
                    SELECT DISCOUNT_RATE
                    FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                    WHERE 
                        TO_NUMBER(REPLACE(DURATION_TYPE, '일 이상')) = 7
                        AND CAR_TYPE = '트럭'
                )
                ELSE 0
            END AS DISCOUNT_RATE
        FROM
            CAR_RENTAL_COMPANY_RENTAL_HISTORY
    ) H
WHERE
    C.CAR_ID = H.CAR_ID
    AND C.CAR_TYPE = '트럭'
ORDER BY
    FEE DESC
    , H.HISTORY_ID DESC



