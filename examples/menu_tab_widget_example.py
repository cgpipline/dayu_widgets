#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################
import functools

from dayu_widgets.badge import MBadge
from dayu_widgets.label import MLabel
from dayu_widgets.menu_tab_widget import MMenuTabWidget
from dayu_widgets.message import MMessage
from dayu_widgets.tool_button import MToolButton
from dayu_widgets import dayu_theme
from dayu_widgets.qt import QWidget,Qt
from dayu_widgets.qt import QVBoxLayout


class MenuTabWidgetExample(QWidget):
    def __init__(self, parent=None):
        super(MenuTabWidgetExample, self).__init__(parent)
        self.setWindowTitle('Examples for MMenuTabWidget')
        self._init_ui()

    def _init_ui(self):
        item_list = [
            {'text': 'Overview', 'svg': 'home_line.svg',
             'clicked': functools.partial(MMessage.info, u'首页', parent=self)},
            {'text': u'我的', 'svg': 'user_line.svg',
             'clicked': functools.partial(MMessage.info, u'编辑账户', parent=self)},
            {'text': u'Notice', 'svg': 'alert_line.svg',
             'clicked': functools.partial(MMessage.info, u'查看通知', parent=self)},
        ]
        tool_bar = MMenuTabWidget()
        tool_bar_huge = MMenuTabWidget()
        tool_bar_huge.set_dayu_size(dayu_theme.huge)
        tool_bar_huge_v = MMenuTabWidget(orientation=Qt.Vertical)
        tool_bar_huge_v.set_dayu_size(dayu_theme.huge)
        tool_bar.tool_bar_insert_widget(MLabel('DaYu').h4().secondary().strong())
        tool_bar_huge.tool_bar_insert_widget(MLabel('DaYu').h4().secondary().strong())
        dayu_icon = MLabel('DaYu').h4().secondary().strong()
        dayu_icon.setContentsMargins(10, 10, 10, 10)
        tool_bar_huge_v.tool_bar_insert_widget(dayu_icon)
        tool_bar.tool_bar_append_widget(
            MBadge.dot(show=True,
                       widget=MToolButton().icon_only().svg('user_fill.svg').large()))
        for index, data_dict in enumerate(item_list):
            tool_bar.add_menu(data_dict, index)
            tool_bar_huge.add_menu(data_dict, index)
            tool_bar_huge_v.add_menu(data_dict, index)

        tool_bar.tool_button_group.set_dayu_checked(0)
        tool_bar_huge.tool_button_group.set_dayu_checked(0)
        tool_bar_huge_v.tool_button_group.set_dayu_checked(0)

        main_lay = QVBoxLayout()
        main_lay.setContentsMargins(0, 0, 0, 0)

        main_lay.addWidget(MLabel('Menu Tab Widget (Large)'))
        main_lay.addWidget(tool_bar)

        main_lay.addWidget(MLabel('Menu Tab Widget (Huge)'))
        main_lay.addWidget(tool_bar_huge)

        main_lay.addWidget(MLabel('Menu Vertical Tab Widget (Huge)'))
        main_lay.addWidget(tool_bar_huge_v)

        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys
    from dayu_widgets.qt import QApplication

    app = QApplication(sys.argv)
    test = MenuTabWidgetExample()
    dayu_theme.apply(test)

    test.show()
    sys.exit(app.exec_())
