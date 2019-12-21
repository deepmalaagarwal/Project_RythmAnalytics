CREATE TABLE "Artists" (
    "id" int   NOT NULL,
    "real_name" VARCHAR   NULL,
	"art_name" VARCHAR   NULL,
	"role" VARCHAR   NULL,
	"year_of_birth" INT   NULL,
	"country" VARCHAR   NULL,
	"city" VARCHAR   NULL,
	"email" VARCHAR   NULL,
	"zip_code" varchar  NULL,
	
    CONSTRAINT "pk_Artists" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "Albums" (
    "id" int   NOT NULL,
    "artist_id" int   NULL,
	"album_title" VARCHAR   NULL,
	"genre" VARCHAR   NULL,
	"year_of_pub" INT   NULL,
	"num_of_tracks" int   NULL,
	"num_of_sales" int   NULL,
	"rolling_stone_critic" decimal   NULL,
	"mtv_critic" decimal  NULL,
	"music_maniac_critic" decimal  NULL,
	
	
    CONSTRAINT "pk_Albums" PRIMARY KEY (
        "id"
     )
);


CREATE TABLE "Rolling_Stones" (
    "rank" int    NULL,
    "song" VARCHAR    NULL,
    "artist" VARCHAR    NULL,
    "year" int    NULL,
    "lyrics" VARCHAR(10000)    NULL,
	"source" VARCHAR    NULL
	
);