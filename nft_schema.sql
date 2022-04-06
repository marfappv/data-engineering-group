-- psql --host=nfts.cuweglfckgza.eu-west-2.rds.amazonaws.com --port=5432 --username=marfapopova21 --password --dbname=nfts

drop schema nfts cascade;
create schema nfts;

drop table if exists nfts.assets cascade;
create table nfts.assets (
    id                      varchar(100),
    creator                 varchar(100),
    artwork_name            varchar(1000),
    collection              varchar(1000),
    currency                varchar(3),
    price                   numeric,
    nsfw                    boolean
);

\dn
\dt nfts.*
select * from nfts.assets;
