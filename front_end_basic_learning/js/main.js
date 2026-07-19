// 作为入口文件，统一调用各个模块的初始化函数

import { initCardsAnim } from "./cards";
import { initNavAnim } from "./nav";
import { initScoreAnim } from "./score";

initCardsAnim();
initNavAnim();
initScoreAnim();
