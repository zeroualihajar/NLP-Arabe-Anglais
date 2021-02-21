import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { TestComponent } from './pages/test/test.component';
import { GraphQLModule } from './graphql.module';
import { HttpClientModule } from '@angular/common/http';
import { MainComponent } from './pages/main/main.component';
import { MainArComponent } from './pages/main-ar/main-ar.component';
import { LoginComponent } from './pages/login/login.component';
import { SignupComponent } from './pages/signup/signup.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ServicesNlpComponent } from './pages/services-nlp/services-nlp.component';
import { PrincipalComponent } from './pages/principal/principal.component';
import { MatCardModule } from '@angular/material/card';
import { DetailsComponent } from './pages/details/details.component';
import { AboutComponent } from './pages/about/about.component';

@NgModule({
  declarations: [
    AppComponent,
    TestComponent,
    MainComponent,
    MainArComponent,
    LoginComponent,
    SignupComponent,
    ServicesNlpComponent,
    PrincipalComponent,
    DetailsComponent,
    AboutComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    GraphQLModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    MatCardModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
