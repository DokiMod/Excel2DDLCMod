# RPY元素与sheet中每列的对应关系
from model.element import Text, Image, Transition, Audio

ElementColNumMapping = {
    'role_name': 0,
    'text': 1,
    'music': 18,
    'character': 19,
    'change_page': 20,
    'background': 21,
    'remark': 22,
    'mode': 23,
    'sound': 24,
    'transition': 25,
    'special': 26,
    'voice': 27,
}

# 元素映射
ElementMapping = {
    "文本": Text,
    "立绘": Image,
    "背景": Image,
    "转场": Transition,
    "音效": Audio,
}

# 位置映射
PositionMapping = {
    "t11": "t11",
    "t21": "t21",
    "t22": "t22",
    "t31": "t31",
    "t32": "t32",
    "t33": "t33",
    "t41": "t41",
    "t42": "t42",
    "t43": "t43",
    "t44": "t44",
    "i11": "i11",
    "i21": "i21",
    "i22": "i22",
    "i31": "i31",
    "i32": "i32",
    "i33": "i33",
    "i41": "i41",
    "i42": "i42",
    "i43": "i43",
    "i44": "i44",
    "f11": "f11",
    "f21": "f21",
    "f22": "f22",
    "f31": "f31",
    "f32": "f32",
    "f33": "f33",
    "f41": "f41",
    "f42": "f42",
    "f43": "f43",
    "f44": "f44",
    "s11": "s11",
    "s21": "s21",
    "s22": "s22",
    "s31": "s31",
    "s32": "s32",
    "s33": "s33",
    "s41": "s41",
    "s42": "s42",
    "s43": "s43",
    "s44": "s44",
    "h11": "h11",
    "h21": "h21",
    "h22": "h22",
    "h31": "h31",
    "h32": "h32",
    "h33": "h33",
    "h41": "h41",
    "h42": "h42",
    "h43": "h43",
    "h44": "h44",
    "hf11": "hf11",
    "hf21": "hf21",
    "hf22": "hf22",
    "hf31": "hf31",
    "hf32": "hf32",
    "hf33": "hf33",
    "hf41": "hf41",
    "hf42": "hf42",
    "hf43": "hf43",
    "hf44": "hf44",
    "d11": "d11",
    "d21": "d21",
    "d22": "d22",
    "d31": "d31",
    "d32": "d32",
    "d33": "d33",
    "d41": "d41",
    "d42": "d42",
    "d43": "d43",
    "d44": "d44",
    "l11": "l11",
    "l21": "l21",
    "l22": "l22",
    "l31": "l31",
    "l32": "l32",
    "l33": "l33",
    "l41": "l41",
    "l42": "l42",
    "l43": "l43",
    "l44": "l44",
    "face": "face",

    "right": "right",
    "mid": "center",
    "truecenter": "truecenter",
}

# 图片指令
ImageCmdMapping = {
    "hide": "hide",
}

# 转场指令
TransitionMapping = {
    "溶解": "dissolve",
    "CG": "dissolve_cg",
    "场景": "dissolve_scene",
    "下一天": "dissolve_scene_full",
    "强切": "dissolve_scene_half",
    "闭眼": "close_eyes",
    "睁眼": "open_eyes",
    "瞬黑": "trueblack",
    "擦除": "wipeleft",
    "场景擦除": "wipeleft_scene",
    # "褪色": "fade",
    # "闪白": "Fade(0.1,0.0,0.5,color=\"#FFFFFF\")",
    # "像素化": "pixellate",
    # "横向振动": "hpunch",
    # "纵向振动": "vpunch",
    # "百叶窗": "blinds",
    # "网格覆盖": "squares",
    # "滑入": "slideleft",
    # "滑出": "slideawayleft",
    # "推出": "pushright",
}

# 音效指令
SoundCmdMapping = {
    "循环": "loop"
}

ReplaceCharacterMapping = {
    "%": "\\%",  # % --> \%
    "\"": "\\\"",  # " -> \"
    "\'": "\\\'",  # ' -> \'
    "{": "{{",  # { -> {{
    "[": "[[",  # [ -> [[
}
