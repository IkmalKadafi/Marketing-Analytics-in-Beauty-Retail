# Handle Missing Values
SELECT *,
  COALESCE(clicks, 0) AS clicks_clean,
  COALESCE(add_to_cart, 0) AS atc_clean,
  COALESCE(conversions, 0) AS conversions_clean
FROM campaign_data;

# Funnel Logic Check
SELECT *,
  CASE 
    WHEN clicks > impressions THEN 1
    WHEN add_to_cart > clicks THEN 1
    WHEN conversions > add_to_cart THEN 1
    ELSE 0
  END AS is_funnel_error
FROM campaign_data;

# Create Clean View
CREATE VIEW clean_funnel_campaign_data AS
SELECT *
FROM campaign_data
WHERE 
  clicks <= impressions
  AND add_to_cart <= clicks
  AND conversions <= add_to_cart;

SELECT * FROM clean_funnel_campaign_data;

SELECT
    CASE
        WHEN clicks > impressions
        OR add_to_cart > clicks
        OR conversions > add_to_cart THEN 'Error'
        ELSE 'Normal'
    END AS status,
    COUNT(*) AS total,
    ROUND(
        COUNT(*) * 100.0 / (
            SELECT COUNT(*)
            FROM campaign_data
        ),
        2
    ) AS percentage
FROM campaign_data
GROUP BY
    status;

# Feature Engineering
SELECT *,
  IFNULL(clicks / NULLIF(impressions, 0), 0) AS ctr,
  IFNULL(add_to_cart / NULLIF(clicks, 0), 0) AS atc_rate,
  IFNULL(conversions / NULLIF(clicks, 0), 0) AS conversion_rate,
  IFNULL(cost / NULLIF(clicks, 0), 0) AS cpc,
  IFNULL(cost / NULLIF(conversions, 0), 0) AS cpa,
  IFNULL(revenue / NULLIF(cost, 0), 0) AS roas,
  IFNULL((revenue - cost) / NULLIF(cost, 0), 0) AS roi
FROM clean_funnel_campaign_data;