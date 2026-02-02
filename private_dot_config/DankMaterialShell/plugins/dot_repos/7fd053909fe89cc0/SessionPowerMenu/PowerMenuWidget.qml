import QtQuick
import QtQuick.Layouts
import Quickshell
import qs.Common
import qs.Services
import qs.Widgets
import qs.Modules.Plugins

PluginComponent {
    id: root

    horizontalBarPill: Component {
        DankIcon {
            name: "power_settings_new"
            anchors.centerIn: parent
        }
    }

    verticalBarPill: Component {
        DankIcon {
            name: "power_settings_new"
            anchors.centerIn: parent
        }
    }

    popoutContent: Component {
        PopoutComponent {
            id: popout
            showCloseButton: false

            Column {
                width: parent.width - Theme.spacingM
                anchors.horizontalCenter: parent.horizontalCenter
                topPadding: Theme.spacingS
                bottomPadding: Theme.spacingS
                spacing: Theme.spacingXS

                // Header
                StyledText {
                    text: "Power Options"
                    font.pixelSize: Theme.fontSizeMedium
                    font.weight: Font.Medium
                    color: Theme.surfaceText
                    width: parent.width
                    bottomPadding: Theme.spacingXS
                }

                ColumnLayout {
                    width: parent.width
                    spacing: Theme.spacingXS

                    // Logout
                    Rectangle {
                        Layout.fillWidth: true
                        height: 36
                        radius: 6
                        color: logoutMouseArea.containsMouse ? Qt.rgba(Theme.surfaceText.r, Theme.surfaceText.g, Theme.surfaceText.b, 0.1) : "transparent"

                        Behavior on color { ColorAnimation { duration: 150 } }

                        RowLayout {
                            anchors {
                                fill: parent
                                leftMargin: Theme.spacingS
                                rightMargin: Theme.spacingS
                            }
                            spacing: Theme.spacingS

                            DankIcon {
                                name: "logout"
                                size: Theme.iconSize
                                color: Theme.surfaceText
                            }

                            StyledText {
                                text: "Log Out"
                                font.pixelSize: Theme.fontSizeSmall
                                color: Theme.surfaceText
                                Layout.fillWidth: true
                            }
                        }

                        MouseArea {
                            id: logoutMouseArea
                            anchors.fill: parent
                            hoverEnabled: true
                            cursorShape: Qt.PointingHandCursor
                            onClicked: {
                                popout.closePopout()
                                SessionService.logout()
                            }
                        }
                    }

                    // Reboot
                    Rectangle {
                        Layout.fillWidth: true
                        height: 36
                        radius: 6
                        color: rebootMouseArea.containsMouse ? Qt.rgba(Theme.surfaceText.r, Theme.surfaceText.g, Theme.surfaceText.b, 0.1) : "transparent"

                        Behavior on color { ColorAnimation { duration: 150 } }

                        RowLayout {
                            anchors {
                                fill: parent
                                leftMargin: Theme.spacingS
                                rightMargin: Theme.spacingS
                            }
                            spacing: Theme.spacingS

                            DankIcon {
                                name: "restart_alt"
                                size: Theme.iconSize
                                color: Theme.surfaceText
                            }

                            StyledText {
                                text: "Reboot"
                                font.pixelSize: Theme.fontSizeSmall
                                color: Theme.surfaceText
                                Layout.fillWidth: true
                            }
                        }

                        MouseArea {
                            id: rebootMouseArea
                            anchors.fill: parent
                            hoverEnabled: true
                            cursorShape: Qt.PointingHandCursor
                            onClicked: {
                                popout.closePopout()
                                SessionService.reboot()
                            }
                        }
                    }

                    // Shutdown
                    Rectangle {
                        Layout.fillWidth: true
                        height: 36
                        radius: 6
                        color: shutdownMouseArea.containsMouse ? Qt.rgba(Theme.surfaceText.r, Theme.surfaceText.g, Theme.surfaceText.b, 0.1) : "transparent"

                        Behavior on color { ColorAnimation { duration: 150 } }

                        RowLayout {
                            anchors {
                                fill: parent
                                leftMargin: Theme.spacingS
                                rightMargin: Theme.spacingS
                            }
                            spacing: Theme.spacingS

                            DankIcon {
                                name: "power_settings_new"
                                size: Theme.iconSize
                                color: Theme.surfaceText
                            }

                            StyledText {
                                text: "Shutdown"
                                font.pixelSize: Theme.fontSizeSmall
                                color: Theme.surfaceText
                                Layout.fillWidth: true
                            }
                        }

                        MouseArea {
                            id: shutdownMouseArea
                            anchors.fill: parent
                            hoverEnabled: true
                            cursorShape: Qt.PointingHandCursor
                            onClicked: {
                                popout.closePopout()
                                SessionService.poweroff()
                            }
                        }
                    }

                    // Lock (if available)
                    Rectangle {
                        Layout.fillWidth: true
                        height: 36
                        radius: 6
                        visible: SessionService.lockSupported !== false
                        color: lockMouseArea.containsMouse ? Qt.rgba(Theme.surfaceText.r, Theme.surfaceText.g, Theme.surfaceText.b, 0.1) : "transparent"

                        Behavior on color { ColorAnimation { duration: 150 } }

                        RowLayout {
                            anchors {
                                fill: parent
                                leftMargin: Theme.spacingS
                                rightMargin: Theme.spacingS
                            }
                            spacing: Theme.spacingS

                            DankIcon {
                                name: "lock"
                                size: Theme.iconSize
                                color: Theme.surfaceText
                            }

                            StyledText {
                                text: "Lock"
                                font.pixelSize: Theme.fontSizeSmall
                                color: Theme.surfaceText
                                Layout.fillWidth: true
                            }
                        }

                        MouseArea {
                            id: lockMouseArea
                            anchors.fill: parent
                            hoverEnabled: true
                            cursorShape: Qt.PointingHandCursor
                            onClicked: {
                                popout.closePopout()
                                // Use loginctl to lock the session
                                Quickshell.execDetached(["loginctl", "lock-session"])
                            }
                        }
                    }

                    // Suspend (if available)
                    Rectangle {
                        Layout.fillWidth: true
                        height: 36
                        radius: 6
                        visible: SessionService.suspendSupported !== false
                        color: suspendMouseArea.containsMouse ? Qt.rgba(Theme.surfaceText.r, Theme.surfaceText.g, Theme.surfaceText.b, 0.1) : "transparent"

                        Behavior on color { ColorAnimation { duration: 150 } }

                        RowLayout {
                            anchors {
                                fill: parent
                                leftMargin: Theme.spacingS
                                rightMargin: Theme.spacingS
                            }
                            spacing: Theme.spacingS

                            DankIcon {
                                name: "bedtime"
                                size: Theme.iconSize
                                color: Theme.surfaceText
                            }

                            StyledText {
                                text: "Suspend"
                                font.pixelSize: Theme.fontSizeSmall
                                color: Theme.surfaceText
                                Layout.fillWidth: true
                            }
                        }

                        MouseArea {
                            id: suspendMouseArea
                            anchors.fill: parent
                            hoverEnabled: true
                            cursorShape: Qt.PointingHandCursor
                            onClicked: {
                                popout.closePopout()
                                SessionService.suspend()
                            }
                        }
                    }
                }
            }
        }
    }

    popoutWidth: 200
}
