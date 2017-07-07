

## VPN

http://lifehacker.com/how-to-set-up-your-own-completely-free-vpn-in-the-cloud-1794302432

http://www.slate.com/articles/technology/future_tense/2017/02/how_to_set_up_a_virtual_private_network.html

http://www.techhive.com/article/3158192/privacy/howand-whyyou-should-use-a-vpn-any-time-you-hop-on-the-internet.html

https://www.howtogeek.com/221001/how-to-set-up-your-own-home-vpn-server/

http://www.practicallynetworked.com/security/set-up-a-personal-windows-vpn.htm







##  automated web testing tool



https://automatetheboringstuff.com/chapter11/

https://mentormate.com/blog/complete-guide-automated-software-testing-tools-comparison/

http://www.discoversdk.com/blog/web-scraping-with-selenium





## powershell

New-NetFirewallRule -DisplayName 'HTTP(S) Inbound' -Profile @('Domain', 'Private') -Direction Inbound -Action Allow -Protocol TCP -LocalPort @('80', '443')

netsh advfirewall firewall add rule name="Open Port 443" dir=in action=allow protocol=TCP localport=443

```
Test-NetConnection -Port 80 -InformationLevel Detailed
```

## Ruby

http://blog.teamtreehouse.com/installing-rails-5-windows

ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCoS/+WQRQv342FQD7ubJtOnZiTo6NiIeADXTrI7eXuZGjLcOISY4qvj+bWzoJMywAqhMsGywHj4f2LbRrLd7WnyagBi9lWvnMEQ9QkKYcv0tz+k/FAldS8vDiRnpxg9EdSx5Qua6hfMQIRkj7t3nSguZuVTuMLGKLDIJdF3ODePFywEDhpRjlsz4FhPLx6OQQ3PlvH8HbzMW0TBssb8rN7GbjuPHC1AK+ZcvL8mJwGA/bG7q6SoMNTZi7k/b4Ci8KzjwXuKY1K3yb7YavGxlZNN/W4HUXMoUiOBO2pSwhpp8TyrbIlWSVJQ52pHNgVoWm+M1siJynwZCYOfaGpEG8d axuaxu <axu0110@gmail.com>

http://guides.rubyonrails.org/

http://railsinstaller.org/en

http://jekyll-windows.juthilo.com/1-ruby-and-devkit/

https://gorails.com/setup/ubuntu/16.04

ssh:
  public_key_location: C:\Users\axu/.ssh/id_rsa.pub
  public_key_contents: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCoS/+WQRQv342FQD7ubJtOnZiTo6NiIeADXTrI7eXuZGjLcOISY4qvj+bWzoJMywAqhMsGywHj4f2LbRrLd7WnyagBi9lWvnMEQ9QkKYcv0tz+k/FAldS8vDiRnpxg9EdSx5Qua6hfMQIRkj7t3nSguZuVTuMLGKLDIJdF3ODePFywEDhpRjlsz4FhPLx6OQQ3PlvH8HbzMW0TBssb8rN7GbjuPHC1AK+ZcvL8mJwGA/bG7q6SoMNTZi7k/b4Ci8KzjwXuKY1K3yb7YavGxlZNN/W4HUXMoUiOBO2pSwhpp8TyrbIlWSVJQ52pHNgVoWm+M1siJynwZCYOfaGpEG8d axuaxu <axu0110@gmail.com>


NOTES:

  Your public ssh key (id_rsa.pub) has been automatically generated and copied to your clipboard.

## chrome on linux

gem chromedriver-helper

https://chromedriver.storage.googleapis.com/index.html?path=2.9/

https://askubuntu.com/questions/510056/how-to-install-google-chrome

## X11 for windows

https://www.youtube.com/watch?v=19UK_qK5zTA

http://www.geo.mtu.edu/geoschem/docs/putty_install.html

https://askubuntu.com/questions/508410/after-install-google-chrome-in-ec2-wont-open-from-ubuntu-server-14-04-lts-hvm