CREATE TABLE `stat` (
      `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
      `host` varchar(256) DEFAULT NULL,
      `mem_free` int(11) DEFAULT NULL,
      `mem_usage` int(11) DEFAULT NULL,
      `mem_total` int(11) DEFAULT NULL,
      `load_avg` varchar(128) DEFAULT NULL,
      `time` bigint(11) DEFAULT NULL,
      PRIMARY KEY (`id`),
      KEY `host` (`host`(255))
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;
