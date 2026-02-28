-- Step 1: Retrieve the IBANs for the specified company
SELECT 
    SUM(t."Amount (EUR)") AS "Current Balance"
FROM (
    -- Step 2: Process SEPA transactions
    SELECT 
        CASE
            WHEN s.payer IN (
                SELECT ibans 
                FROM company_df 
                WHERE name = '<company_name>'
            ) THEN -s.amount / ex.eur_rate
            ELSE s.amount / ex.eur_rate
        END AS "Amount (EUR)"
    FROM sepa_df s
    LEFT JOIN exchange_df ex ON s.currency = ex.currency
    WHERE s.payer IN (
        SELECT ibans 
        FROM company_df 
        WHERE name = '<company_name>'
    ) 
    OR s.receiver IN (
        SELECT ibans 
        FROM company_df 
        WHERE name = '<company_name>'
    )

    UNION ALL

    -- Step 3: Process SWIFT transactions
    SELECT 
        CASE
            WHEN w.sender IN (
                SELECT ibans 
                FROM company_df 
                WHERE name = '<company_name>'
            ) THEN -w.amount / ex.eur_rate
            ELSE w.amount / ex.eur_rate
        END AS "Amount (EUR)"
    FROM swift_df w
    LEFT JOIN exchange_df ex ON w.currency = ex.currency
    WHERE w.sender IN (
        SELECT ibans 
        FROM company_df 
        WHERE name = '<company_name>'
    ) 
    OR w.beneficiary IN (
        SELECT ibans 
        FROM company_df 
        WHERE name = '<company_name>'
    )
) t;
