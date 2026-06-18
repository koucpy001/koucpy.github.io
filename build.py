#!/usr/bin/env python3
"""Read nav-data.json and generate cn/index.html"""

import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(SCRIPT_DIR, "nav-data.json")
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "cn", "index.html")
ICON_DIR = "../assets/images/logos"


def site_card(site):
    icon_path = f"{ICON_DIR}/{site.get('icon', 'default.png')}"
    return f'''                <div class="col-sm-3">
                    <div class="xe-widget xe-conversations box2 label-info" onclick="window.open('{site['url']}', '_blank')" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="{site['url']}">
                        <div class="xe-comment-entry">
                            <a class="xe-user-img">
                                <img src="{icon_path}" class="lozad img-circle" width="40">
                            </a>
                            <div class="xe-comment">
                                <a href="#" class="xe-user-name overflowClip_1">
                                    <strong>{site['name']}</strong>
                                </a>
                                <p class="overflowClip_2">{site['desc']}</p>
                            </div>
                        </div>
                    </div>
                </div>'''


def sidebar_item(cat):
    if not cat.get("subcategories"):
        return f'''                    <li>
                        <a href="#{cat['name']}" class="smooth">
                            <i class="{cat['icon']}"></i>
                            <span class="title">{cat['name']}</span>
                        </a>
                    </li>'''
    subs = "\n".join(
        f'                            <li><a href="#{s}" class="smooth"><span class="title">{s}</span></a></li>'
        for s in cat["subcategories"]
    )
    return f'''                    <li class="has-sub">
                        <a href="javascript:void(0)">
                            <i class="{cat['icon']}"></i>
                            <span class="title">{cat['name']}</span>
                        </a>
                        <ul>
{subs}
                        </ul>
                    </li>'''


def content_section(sec):
    rows = []
    sites = sec["sites"]
    for i in range(0, len(sites), 4):
        chunk = sites[i : i + 4]
        cards = "\n".join(site_card(s) for s in chunk)
        rows.append(f'            <div class="row">\n{cards}\n            </div>')
    rows_html = "\n".join(rows)
    return f'''            <h4 class="text-gray"><i class="{sec['icon']}" style="margin-right: 7px;" id="{sec['id']}"></i>{sec['id']}</h4>
{rows_html}'''


def build():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    site = data["site"]
    categories = data["categories"]
    sections = data["sections"]

    sidebar = "\n".join(sidebar_item(c) for c in categories)
    content = "\n".join(content_section(s) for s in sections)

    html = f'''<!DOCTYPE html>
<html lang="zh">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="author" content="{site['author']}" />
    <title>{site['title']}</title>
    <meta name="keywords" content="{site['keywords']}">
    <meta name="description" content="{site['description']}">
    <link rel="shortcut icon" href="../assets/images/favicon.png">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Arimo:400,700,400italic">
    <link rel="stylesheet" href="../assets/css/fonts/linecons/css/linecons.css">
    <link rel="stylesheet" href="../assets/css/fonts/fontawesome/css/font-awesome.min.css">
    <link rel="stylesheet" href="../assets/css/bootstrap.css">
    <link rel="stylesheet" href="../assets/css/xenon-core.css">
    <link rel="stylesheet" href="../assets/css/xenon-components.css">
    <link rel="stylesheet" href="../assets/css/xenon-skins.css">
    <link rel="stylesheet" href="../assets/css/nav.css">
    <script src="../assets/js/jquery-1.11.1.min.js"></script>
</head>

<body class="page-body">
    <div class="page-container">
        <div class="sidebar-menu toggle-others fixed">
            <div class="sidebar-menu-inner">
                <header class="logo-env">
                    <div class="logo">
                        <a href="index.html" class="logo-expanded">
                            <img src="../assets/images/logo@2x.png" width="100%" alt="" />
                        </a>
                        <a href="index.html" class="logo-collapsed">
                            <img src="../assets/images/logo-collapsed@2x.png" width="40" alt="" />
                        </a>
                    </div>
                    <div class="mobile-menu-toggle visible-xs">
                        <a href="#" data-toggle="user-info-menu">
                            <i class="linecons-cog"></i>
                        </a>
                        <a href="#" data-toggle="mobile-menu">
                            <i class="fa-bars"></i>
                        </a>
                    </div>
                </header>
                <ul id="main-menu" class="main-menu">
{sidebar}
                    <li>
                        <a href="about.html">
                            <i class="linecons-heart"></i>
                            <span class="tooltip-blue">关于本站</span>
                            <span class="label label-Primary pull-right hidden-collapsed">♥︎</span>
                        </a>
                    </li>
                </ul>
            </div>
        </div>
        <div class="main-content">
            <nav class="navbar user-info-navbar" role="navigation">
                <ul class="user-info-menu left-links list-inline list-unstyled">
                    <li class="hidden-sm hidden-xs">
                        <a href="#" data-toggle="sidebar">
                            <i class="fa-bars"></i>
                        </a>
                    </li>
                    <li class="dropdown hover-line language-switcher">
                        <a href="../cn/index.html" class="dropdown-toggle" data-toggle="dropdown">
                            <img src="../assets/images/flags/flag-cn.png" alt="flag-cn" /> Chinese
                        </a>
                        <ul class="dropdown-menu languages">
                            <li>
                                <a href="../en/index.html">
                                    <img src="../assets/images/flags/flag-us.png" alt="flag-us" /> English
                                </a>
                            </li>
                            <li class="active">
                                <a href="../cn/index.html">
                                    <img src="../assets/images/flags/flag-cn.png" alt="flag-cn" /> Chinese
                                </a>
                            </li>
                        </ul>
                    </li>
                </ul>
                <ul class="user-info-menu right-links list-inline list-unstyled">
                    <li class="hidden-sm hidden-xs">
                        <a href="{site['github']}" target="_blank">
                            <i class="fa-github"></i> GitHub
                        </a>
                    </li>
                </ul>
            </nav>

{content}

            <!-- Footer -->
            <footer class="main-footer sticky-footer">
                <div class="footer-inner">
                    <div class="footer-text">
                        &copy; 2024 <a href="{site['github']}" target="_blank">{site['author']}</a> | Based on <a href="https://github.com/WebStackPage/WebStackPage.github.io" target="_blank">WebStack</a>
                    </div>
                </div>
            </footer>
        </div>
    </div>

    <!-- Bottom Scripts -->
    <script src="../assets/js/bootstrap.min.js"></script>
    <script src="../assets/js/TweenMax.min.js"></script>
    <script src="../assets/js/resizeable.js"></script>
    <script src="../assets/js/joinable.js"></script>
    <script src="../assets/js/xenon-api.js"></script>
    <script src="../assets/js/xenon-toggles.js"></script>
    <script src="../assets/js/xenon-custom.js"></script>
    <script src="../assets/js/lozad.js"></script>
    <script>
    jQuery(document).ready(function($) {{
        var $sidebarMenu = $(".sidebar-menu");
        var $mainMenu = $("#main-menu");

        $mainMenu.find("a.smooth").on("click", function(e) {{
            e.preventDefault();
            var target = $(this).attr("href");
            if (target && target.startsWith("#")) {{
                var $target = $(target);
                if ($target.length) {{
                    $("html, body").animate({{
                        scrollTop: $target.offset().top - 30
                    }}, 500);
                }}
            }}
        }});

        var observer = lozad();
        observer.observe();
    }});
    </script>
</body>

</html>
'''

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Built {OUTPUT_FILE} ({len(html)} bytes)")


if __name__ == "__main__":
    build()
