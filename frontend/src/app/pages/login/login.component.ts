import { LoginService } from './../../services/login/login.service';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';



@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  form!: FormGroup;

  constructor(private formBuilder: FormBuilder, private loginService:LoginService) { }

  ngOnInit(): void {
    this.form = this.formBuilder.group({
      email : new FormControl('', Validators.required),
      password : new FormControl('', Validators.required),
    })
  }

  confirm() {

    this.loginService.loginQuery(this.form)
    }

}
