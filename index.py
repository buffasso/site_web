__author__ = 'desilvsa'
template=Import('template.py')

def qui():
    qui = '''<div class="section mcontainer description">
                    <h2>Qui sommes-nous ?</h2>
                    <div class="container">
                        <p>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.<br/>

                            Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur.<br/>
                            Adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?
                        </p>
                    </div>
                </div>'''
    return qui


def video():
    video = '''<div class="section mcontainer grey darken-4">
                    <h2 class="white-text">Video de campagne</h2>
                    <div class="container">
                        <div class="video-container">
                            <iframe width="100" height="100" src="https://www.youtube.com/embed/VcDy8HEg1QY" frameborder="0" allowfullscreen></iframe>
                        </div>
                    </div>
                </div>'''
    return video


def propose():
    propose = '''<div class="section mcontainer services">
                    <h2>On vous propose ...</h2>
                    <div class="container">
                        <div class="row">
                            <div class="col s12 m4">
                                <div class="icon-block">
                                    <div class="center red-text"><i class="material-icons big_icon">access_time</i></div>
                                    <h5 class="center">Nourriture H24</h5>
                                    <p class="light">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
                                    <div class="center"><a class="waves-effect waves-light btn-large red" href="/site_web/services/nourriture.py/nourriture">Voir</a></div>
                                </div>
                            </div>

                            <div class="col s12 m4">
                                <div class="icon-block">
                                    <div class="center red-text"><i class="material-icons big_icon">restaurant</i></div>
                                    <h5 class="center">Repas</h5>
                                    <p class="light">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
                                    <div class="center"><a class="waves-effect waves-light btn-large red" href="/site_web/services/repas.py/repas">Voir</a></div>
                                </div>
                            </div>

                            <div class="col s12 m4">
                                <div class="icon-block">
                                    <div class="center red-text"><i class="material-icons big_icon">room_service</i></div>
                                    <h5 class="center">Services</h5>
                                    <p class="light">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
                                    <div class="center"><a class="waves-effect waves-light btn-large red" href="/site_web/services/service.py/service">Voir</a></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>'''
    return propose


def scroll():
    scroll = '''<div class="head">
                    <img class="logo"  src="/site_web/assets/imgs/buff.png">
                    <div onclick="scrollDown()">
                        <i class="arrow white-text material-icons">keyboard_arrow_down</i>
                    </div>
                </div>'''
    return scroll


def index():
    result=template.entete('Buff\'asso bill')
    result+=scroll()
    result+=template.nav()
    result+=qui()
    result+=video()
    result+=propose()
    result+=template.footer()
    return result