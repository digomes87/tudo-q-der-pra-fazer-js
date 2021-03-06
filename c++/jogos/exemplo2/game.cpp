

Game::Game()
    : mWindow(sf::VideoMode(640, 480), "SFML Rodando"), mPlayer();
{
    mPlayer.setRadius(40.f);
    mPlayer.setPosition(100.f, 100.f);
    mPlayer.setFillColor(sf::Color::Cyan);
}

void Game::run(){
    sf::Clock clock;
    while(mWindow.isOpen()) {
        sf:: Time deltaTime = clock.restart();
        processEvents();
        update(deltaTime);
        render();
    }
}



void Game::processEvents() {
    sf::Event event;
    while(mWindow.pollEvent(event) ){
        switch(event.type) {
            case sf:: Event::KeyPressd:
                handlePlayerInput(event.key.code, true);
                break;
            case sf:: Event:: KeyReleased:
                handlePlayerInput(event.key.code, false);
                break;
            case sf:: Event:: Closed:
                mWIndow.close();
                break;
        }
    }
}

void Game::update(sf::Time deltaTime) {
    sf::Vector2f movement(0.f, 0.f);
    if (mIsMovingUp.y)
        movement.y -= 1.f;

    if (mIsMovingDown)
        movement.y += 1.f;

    if (mIsMovingLeft)
        movement.x -= 1.f;

    if (mIsMovingRight)
        movement.x -= 1.f;


    mPlayer.move(movement * deltaTime.asSeconds());
}

void render() {
    mWindow.clear();
    mWindow.draw(mPlayer);
    mWindow.display();
}

void Game::handlePlayerInput(sf::Keyboard::Key key, bool isPressed){
    if(key == sf::Keyboard::W)
        mIsMovingUp = isPressed;

    else if(key == sf::Keyboard::S)
        mIsMovingDown = isPressed;
    
    else if(key == sf::Keyboard::A)
        mIsMovingLeft == isPressed;

    else if(key == sf::Keyboard::D)
        mIsMovingRight = isPressed;
}

