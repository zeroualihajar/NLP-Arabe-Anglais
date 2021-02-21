import { AboutComponent } from './pages/about/about.component';
import { PrincipalComponent } from './pages/principal/principal.component';
import { TestComponent } from './pages/test/test.component';
import { MainComponent } from './pages/main/main.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MainArComponent } from './pages/main-ar/main-ar.component';
import { LoginComponent } from './pages/login/login.component';
import { SignupComponent } from './pages/signup/signup.component';
import { GuardGuard } from './pages/guard/guard.guard';
import { DetailsComponent } from './pages/details/details.component';
import { ServicesNlpComponent } from './pages/services-nlp/services-nlp.component';

const routes: Routes = [
  { path: "historique", component: TestComponent},
  { path: "", component: MainComponent},
  { path: "anglais", component: MainArComponent },
  { path: "main", component: MainComponent },
  { path: "login", component: LoginComponent},
  { path: "signup", component: SignupComponent},
  { path: "principal", component: PrincipalComponent},
  { path: "details", component: DetailsComponent},
  { path: "about", component: AboutComponent},
  { path: "emotion", component: ServicesNlpComponent},


];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
