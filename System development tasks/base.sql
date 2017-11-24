
SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `userpwd`
-- ----------------------------
DROP TABLE IF EXISTS `userpwd`;
CREATE TABLE `userpwd` (
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `role` varchar(50) DEFAULT NULL,
  `sex` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of userpwd
-- ----------------------------
INSERT INTO `userpwd` VALUES ('tom', '123', '729926980@qq.com', 'student', 'female');
INSERT INTO `userpwd` VALUES ('sad', 'asd', 'asd@q', 'teacher', 'male');
