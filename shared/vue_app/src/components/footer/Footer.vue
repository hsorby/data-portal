<template>
    <div class="section footer">
        <el-row type="flex" justify="center">
            <el-col :xs="22" :sm="22" :md="22" :lg="18" :xl="16">
                <div class="footer-content">
                    <el-row>
                        <el-col class="contact" :md="8">
                            <sparc-logo class="logo"></sparc-logo>
                            <p class="address">
                                {{ footerAddress.name }}<br/>
                                {{ footerAddress.street }}, {{ footerAddress.city }}, {{ footerAddress.state }}
                            </p>
                            <p class="email-address">
                                {{ footerEmailAddress }}
                            </p>
                            <p class="phone-number">
                                {{ footerPhoneNumber.join("-") }}
                            </p>
                            <div class="social">
                                <p>Twitter</p>
                                <p>Facebook</p>
                            </div>
                            <div class="external-link uppercase">
                                <a href="https://nih.gov">Visit the NIH site ></a>
                            </div>
                        </el-col>
                        <el-col :md="16">
                            <el-row type="flex" class="link-sections">
                                <el-col :key="section.title" :sm="12" :lg="8" class="link-section" v-for="section in footerLinks">
                                    <p class="link-header">{{ section.title }}</p>
                                    <ul>
                                        <li :key="link.title" v-for="link in section.items">
                                            <a :href="link.href">{{ link.title }}</a>
                                        </li>
                                    </ul>
                                </el-col>
                            </el-row>
                        </el-col>
                    </el-row>
                </div>
            </el-col>
        </el-row>
        <el-row type="flex" justify="center">
            <el-col :xs="22" :sm="22" :md="22" :lg="18" :xl="16">
                <div class="legal">
                    <p>NIH Stimulating Peripheral Activity to Relieve Conditions</p>
                    <p>&copy; 2019 All Rights Reserved. <a href="https://blackfynn.com/privacy">Privacy Policy</a>
                    </p>
                </div>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    import SparcLogo from "../logo/SparcLogo.vue";

    const footerAddress = {
        name: "National Institutes of Health",
        street: "990 Rockville Pike",
        city: "Bethesda",
        state: "Maryland"
    }

    const footerEmailAddress = "gene.civillico@nih.gov"

    const footerPhoneNumber = ["301", "451", "3180"]

    const footerTwitterHandle = "/"

    const footerFacebookHandle = "/"

    const footerLinks = [
        {
            title: "Overview",
            items: [
                {
                    title: "Program components",
                    href: "/"
                },
                {
                    title: "SPARC OTs",
                    href: "/"
                },
                {
                    title: "Working group",
                    href: "/"
                }
            ]
        },
        {
            title: "Research",
            items: [
                {
                    title: "Funded research",
                    href: "/"
                },
                {
                    title: "Translational partnerships",
                    href: "/"
                },
                {
                    title: "Opportunities",
                    href: "/"
                },
                {
                    title: "Devices",
                    href: "/"
                },
                {
                    title: "Publications",
                    href: "/"
                }
            ]
        },
        {
            title: "Resources",
            items: [
                {
                    title: "Cores",
                    href: "/"
                },
                {
                    title: "Templates and references",
                    href: "/"
                },
                {
                    title: "Materials",
                    href: "/"
                }
            ]
        },
        {
            title: "News",
            items: [
                {
                    title: "Events",
                    href: "/"
                },
                {
                    title: "Announcements",
                    href: "/"
                }
            ]
        },
        {
            title: "Support",
            items: [
                {
                    title: "Documentation",
                    href: "/"
                },
                {
                    title: "Tutorials",
                    href: "/"
                },
                {
                    title: "Feedback",
                    href: "/"
                }
            ]
        }
    ];

    export default {
        name: "sparc-footer",
        components: {
            SparcLogo
        },
        data: () => ({
            footerLinks,
            footerAddress,
            footerPhoneNumber,
            footerEmailAddress,
            footerTwitterHandle,
            footerFacebookHandle,
        })
    }
</script>

<style scoped lang="scss">
    @import '../../../../../static/css/_variables.scss';

    .footer-content {
        font-size: 10pt;
        size: 10pt;
    }

    .address {
        margin-bottom: 3em;
    }

    .uppercase {
        text-transform: uppercase;
    }


    .footer {
        padding: 6em 0;
        background: #EDF1FC;

        color: #5D6478;
        text-transform: uppercase;
        font-size: 10pt;
        font-weight: 500;

        .link-header {
            color: #000;
        }

        .footer-content {

            .contact {
                margin-bottom: 2em;
            }

            .logo {
                height: 30px;
                margin-bottom: 3em;
            }
        }

    }

    .link-sections {
        display: flex;
        flex-wrap: wrap;
    }

    .link-section {
        padding-bottom: 3em;

        ul {
            list-style-type: none;
            padding: 0;
            margin: 0;

            li {
                padding: .5em 0;
                margin: 0;

                a {
                    color: #606266;
                    text-decoration: none;

                    &:hover {
                        color: #909399;
                    }
                }
            }
        }
    }
</style>