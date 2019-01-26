import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { HttpModule } from '@angular/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { LoginComponent } from './components/login/login.component';
import { InicioComponent } from './components/home/home.component';
import { RegisterComponent } from './components/register/register.component';
import { StatusComponent } from './components/status/status.component';
import { LogoutComponent } from './components/logout/logout.component';
import { UploadComponent } from './components/upload/upload.component';
import { PesquisaComponent } from './components/search/search.component';
import { DetalheComponent } from './components/detail/detail.component';
import { ListFileComponent } from './components/list-file/list-file.component';
import { VizualizacaoComponent } from './components/view/view.component';
import { RequestComponent } from './components/request/request.component';
import { EventComponent } from './components/event/event.component';

import { AuthService } from './services/auth.service';
import { EnsureAuthenticatedService } from './services/ensure-authenticated.service';
import { LoginRedirectService } from './services/login-redirect.service';
import { MenuComponent } from './components/menu/menu.component';
import { LoadingComponent } from './components/loading/loading.component';
import { NotfoundComponent } from './components/notfound/notfound.component';
import { ErrorComponent } from './components/error/error.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    InicioComponent,
    RegisterComponent,
    StatusComponent,
    LogoutComponent,
    UploadComponent,
    PesquisaComponent,
    DetalheComponent,
    ListFileComponent,
    VizualizacaoComponent,
    MenuComponent,
    LoadingComponent,
    RequestComponent,
    EventComponent,
    NotfoundComponent,
    ErrorComponent
  ],
  imports: [
    BrowserModule,
    HttpModule,
    FormsModule,
    ReactiveFormsModule,
    RouterModule.forRoot([
      { path: 'login', component: LoginComponent, canActivate: [LoginRedirectService] },
      { path: 'login/:empresa', component: LoginComponent, canActivate: [LoginRedirectService] },
      { path: 'register', component: RegisterComponent, canActivate: [LoginRedirectService] },
      { path: 'status', component: StatusComponent, canActivate: [EnsureAuthenticatedService] },
      { path: 'upload', component: UploadComponent, canActivate: [EnsureAuthenticatedService] },
      { path: 'search/:text', component: PesquisaComponent, canActivate: [EnsureAuthenticatedService] },
      { path: 'search', component: PesquisaComponent, canActivate: [EnsureAuthenticatedService] },
      { path: 'request', component: RequestComponent, canActivate: [EnsureAuthenticatedService] },
      { path: 'detail/:id', component: DetalheComponent, canActivate: [EnsureAuthenticatedService] },
      { path: 'view/:id', component: VizualizacaoComponent, canActivate: [EnsureAuthenticatedService] },
      { path: 'logout', component: LogoutComponent, canActivate: [EnsureAuthenticatedService] },
      { path: 'new', component: EventComponent, canActivate: [EnsureAuthenticatedService] },
      { path: 'notfound', component: NotfoundComponent, canActivate: [EnsureAuthenticatedService]},
      { path: '', component: InicioComponent, canActivate: [EnsureAuthenticatedService]},
      { path: '**', redirectTo: 'notfound'}
    ])
  ],
  providers: [
    AuthService,
    EnsureAuthenticatedService,
    LoginRedirectService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
