-- Active: 1776175317161@@interchange.proxy.rlwy.net@21491@railway
-- Active: 1776175317161@@interchange.proxy.rlwy.net@21491@mysql
DROP TABLE IF EXISTS campaign_data;

CREATE TABLE campaign_data (
    date DATE,
    channel VARCHAR(100),
    campaign_name VARCHAR(255),
    campaign_type VARCHAR(100),
    region VARCHAR(100),
    device VARCHAR(50),
    audience_age_group VARCHAR(50),
    product_category VARCHAR(100),
    product_price_tier VARCHAR(50),
    impressions INT,
    clicks INT,
    add_to_cart INT,
    conversions INT,
    cost DECIMAL(12, 2),
    revenue DECIMAL(12, 2)
);

LOAD DATA LOCAL INFILE 'D:/Kadafi workspace/Personal Web/Marketing-Analytics-in-Beauty-Retail/campaign_data.sql' INTO
TABLE campaign_data CHARACTER SET utf8mb4 FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS (
    date,
    channel,
    campaign_name,
    campaign_type,
    region,
    device,
    audience_age_group,
    product_category,
    product_price_tier,
    impressions,
    clicks,
    add_to_cart,
    conversions,
    @cost,
    @revenue
)
SET
    cost =
REPLACE (
        REPLACE (@cost, '.', ''),
            ',',
            '.'
    ),
    revenue =
REPLACE (
        REPLACE (@revenue, '.', ''),
            ',',
            '.'
    );

SELECT * FROM campaign_data;