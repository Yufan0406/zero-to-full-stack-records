// 作为入口文件，统一调用各个模块的初始化函数

import { initCardsAnim } from "./cards.js";
import { initNavAnim } from "./nav.js";
import { initScoreAnim } from "./score.js";

initCardsAnim();
initNavAnim();
initScoreAnim();
