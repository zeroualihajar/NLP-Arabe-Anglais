import { Component } from '@angular/core';
import { LoginComponent } from './pages/login/login.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'frontend';

  isDisabled: boolean = true;

  logout(){
    LoginComponent.isLogged = false
    LoginComponent.id = "603196b53af15dfe6dc4174b"
    this.isDisabled = false;
  }
}
