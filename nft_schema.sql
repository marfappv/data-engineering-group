drop schema nfts cascade;
create schema nfts;

drop table if exists nfts.assets cascade;
create table nfts.assets (
    id                      serial primary key,
    creator                 varchar(100),
    artwork_name            varchar(1000),
    collection              varchar(1000),
    price                   numeric,
    nsfw                    boolean
);

\dn
\dt nfts.*
select * from nfts.assets;
