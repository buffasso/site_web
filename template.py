

def entete(page_title):
    entete = '''<!DOCTYPE html>
                    <html lang="fr">
                    <head>
                        <meta charset="UTF-8">
                        <link rel="icon" href="/site_web/assets/imgs/favicon.ico" />
                        <title>Buff'asso bill</title>
                        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
                        <link href="http://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
                        <link rel="stylesheet" href="/site_web/assets/css/materialize.min.css">
                        <link rel="stylesheet" type="text/css" href="/site_web/assets/css/slick.css"/>
                        <link rel="stylesheet" href="/site_web/assets/css/font-awesome.min.css">
                        <link rel="stylesheet" href="/site_web/assets/css/style.css">
                    </head>
                    <body>'''
    return entete


def nav():
    nav = '''<ul id="servicesDrop" class="dropdown-content">
                <li class="itemDrop"><a href="/site_web/services/nourriture.py/nourriture">Nourriture H24</a></li>
                <li class="itemDrop"><a href="/site_web/services/repas.py/repas">Repas</a></li>
                <li class="itemDrop"><a href="/site_web/services/service.py/service">Services</a></li>
            </ul>
            <ul id="polesDrop" class="dropdown-content black-text">
                <li class="itemDrop"><a href="/site_web/poles/bureau.py/bureau">Bureau</a></li>
                <li class="itemDrop"><a href="/site_web/poles/logistique.py/logistique">Logistique</a></li>
                <li class="itemDrop"><a href="/site_web/poles/communication.py/communication">Communication</a></li>
                <li class="itemDrop"><a href="/site_web/poles/partenaire.py/partenaire">Partenaire</a></li>
            </ul>
            <nav class="brown" id="navbar">
                <div class="nav-wrapper">
                    <a href="/site_web/index.py/index#navbar" class="brand-logo">Buff'asso bill</a>
                    <a href="" data-activates="mobile-demo" class="button-collapse"><i class="material-icons">menu</i></a>
                    <ul class="right hide-on-med-and-down">
                        <li><a href="/site_web/planning.py/planning">Planning <i class="material-icons right">date_range</i></a></li>
                        <!--Réfère a la liste ayant le même id dans "data-activates" au dessus-->
                        <li><a class="dropdown-button" href="#" data-activates="polesDrop", style="width:150px">Pôles<i class="material-icons right">arrow_drop_down</i></a></li>
                        <!--Réfère a la liste ayant le même id dans "data-activates" au dessus-->
                        <li><a class="dropdown-button" href="#" data-activates="servicesDrop">Services<i class="material-icons right">arrow_drop_down</i></a></li>
                        <li><a href="#">Espace Perso<i class="material-icons right">person</i></a></li>
                    </ul>
                    <ul class="side-nav" id="mobile-demo">
                        <li><a href="planning.html">Planning</a></li>
                        <li class="divider"></li>
                        <li><a href="/site_web/services/nourriture.py/nourriture">Nourriture H24</a></li>
                        <li><a href="/site_web/services/repas.py/repas">Repas</a></li>
                        <li><a href="/site_web/services/service.py/service">Services</a></li>
                        <li class="divider"></li>
                        <li><a href="/site_web/poles/bureau.py/bureau">Bureau</a></li>
                        <li><a href="/site_web/poles/logistique.py/logistique">Logistique</a></li>
                        <li><a href="/site_web/poles/communication.py/communication">Communication</a></li>
                        <li><a href="/site_web/poles/partenaire.py/partenaire">Partenaire</a></li>
                        <li class="divider"></li>
                        <li><a href="#">Espace perso</a></li>
                    </ul>
                </div>
            </nav>'''
    return nav



def footer():
    footer = '''<footer class="page-footer brown">
                    <div class="container">
                        <div class="row">
                            <div class="col l6 s12 flex_center">
                                <div>
                                    <img height="100" src="/site_web/assets/imgs/buff_logo.png" class="img-responsive">
                                </div>
                                <h6 class="white-text">Buff'asso bill</h6>
                            </div>
                            <div class="col l4 offset-l2 s12">
                                <h5 class="white-text">Partenaires</h5>
                                <ul>
                                    <a href="http://www.cinemasgaumontpathe.com/" target="_blank"><img src="/site_web/assets/imgs/gaumont.png" width="100" alt=""/></a>
                                    <a href="http://www.e-leclerc.com/" target="_blank"><img src="/site_web/assets/imgs/leclerc.png" width="100"/></a>
                                    <a href="https://www.monin.com/fr/home" target="_blank"><img src="/site_web/assets/imgs/monin.png" width="100"/></a>
                                    <a href="http://www.caliceo.com/" target="_blank"><img src="/site_web/assets/imgs/caliceo.png" width="100"/></a>
                                    <a href="https://www.boulanger.com/" target="_blank"><img src="/site_web/assets/imgs/boulanger.png" width="100"/></a>
                                    <a href="https://www.faguo-store.com/fr/" target="_blank"><img src="/site_web/assets/imgs/faguo.png" width="100"/></a>
                                    <a href="http://vandb.fr/" target="_blank"><img src="/site_web/assets/imgs/vb.png" width="100"/></a>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <div class="footer-copyright">
                        <div class="container">
                            © 2017 Buff'asso bill
                        </div>
                    </div>
                </footer>
                <script src="/site_web/assets/js/jquery.min.js"></script>
                <script src="/site_web/assets/js/materialize.min.js"></script>
                <script type="text/javascript" src="/site_web/assets/js/slick.min.js"></script>
                <script src="/site_web/assets/js/script.js"></script>
                </body>
                </html>'''
    return footer