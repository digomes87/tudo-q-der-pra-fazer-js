

Game::Game()
    : mWindow(sf::VideoMode(640, 480), "SFML Rodando"), mPlayer();
{
    mPlayer.setRadius(40.f);
    mPlayer.setPosition(100.f, 100.f);
    mPlayer.setFillColor(sf::Color::Cyan);
}

void Game(){
    while(mWindow.isOpen() )
        processEvents();
        update() ;
        render();
}



void Game::processEvents() {
    sf::Event event;
    while(mWindow.pollEvent(event) ){
        if(event.type == sf::Event::Closed)
            mWIndow.close() ;
    }
}

void update() {
    
}

void render() {
    mWindow.clear();
    mWindow.draw(mPlayer);
    mWindow.display();
}
