psql -h depgdb.crhso94tou3n.eu-west-2.rds.amazonaws.com -d marfapopova21 -U marfapopova21

drop schema nfts cascade;
create schema nfts;

drop table if exists nfts.sources cascade;
create table nfts.sources (
    image_url_asset         varchar(10000), -- character limit for all URLs needs to be huge
    image_url_collection    varchar(10000),
    banner_image_url        varchar(10000),
    background_colour       varchar(100)
);

drop table if exists nfts.product cascade;
create table nfts.product (
    id                      serial primary key,
    token_id                varchar(100),
    name                    varchar(1000),
    externam_link           varchar(1000),
    asset_contract          varchar(1000),
    owner                   varchar(1000),
    traits                  varchar(1000),
    last_sale               timestamp,
    editors                 varchar(1000)
);


drop table if exists nfts.finance_ops cascade;
create table nfts.finance_ops (
    token_id                int references nfts.product("token_id"),
    last_sale               int references nfts.product("last_sale"),
    event_type
    asset_contractasset_bundle
    created_date
    from_aacount
    to_account
    is_privaste
    payment_token
    quantity
    total_price
    dev_seller_fee_basis_points
    payout_address
);

drop table if exists nfts.collections cascade;
create table nfts.collections (
    name                varchar(1000),
    external_link       varchar(1000),
    description         varchar(1000),
    slug                varchar(1000),
    image_url_asset     varchar(1000)
    banner_image_url            varchar(1000),
    dev_seller_fee_basis_points varchar(1000),
    safelist_request_status     varchar(1000),
    payout_address              varchar(1000),
    primary_asset_contracts     varchar(1000),
    traits                      varchar(1000),
    payment_tokens              varchar(1000),
    editors                     varchar(1000),
    stats                       varchar(1000)
);